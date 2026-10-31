"""
Mybizz CS — Vault Service Tests
Phase 0 Implementation — TODO 2
"""
import pytest
from unittest.mock import patch, Mock
import sys
import os

# Add server_code to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'server_code'))

from server_shared.exceptions import VaultError, VaultSecretNotFoundError, VaultDecryptionError
from server_shared.encryption_service import encrypt, decrypt

class TestEncryptionService:
    """Tests for encryption_service.py"""
    
    @patch('anvil.server.secret')
    def test_encrypt_decrypt_roundtrip(self, mock_secret):
        """Test that encrypt and decrypt are inverse operations."""
        mock_secret.return_value = 'test_encryption_key_32_chars_long!!!!'
        
        original = "My secret password 123!"
        encrypted = encrypt(original)
        decrypted = decrypt(encrypted)
        
        assert decrypted == original
        assert encrypted != original
        assert len(encrypted) > len(original)  # IV + padding adds length
    
    @patch('anvil.server.secret')
    def test_different_inputs_produce_different_outputs(self, mock_secret):
        """Test that different inputs produce different encrypted outputs."""
        mock_secret.return_value = 'test_encryption_key_32_chars_long!!!!'
        
        encrypted1 = encrypt("secret1")
        encrypted2 = encrypt("secret2")
        
        assert encrypted1 != encrypted2
    
    @patch('anvil.server.secret')
    def test_empty_string(self, mock_secret):
        """Test encryption/decryption of empty string."""
        mock_secret.return_value = 'test_encryption_key_32_chars_long!!!!'
        
        original = ""
        encrypted = encrypt(original)
        decrypted = decrypt(encrypted)
        
        assert decrypted == original
    
    @patch('anvil.server.secret')
    def test_special_characters(self, mock_secret):
        """Test encryption/decryption with special characters."""
        mock_secret.return_value = 'test_encryption_key_32_chars_long!!!!'
        
        original = "Special chars: @#$%^&*()_+-=[]{}|;':\",./<>?"
        encrypted = encrypt(original)
        decrypted = decrypt(encrypted)
        
        assert decrypted == original

class TestVaultService:
    """Tests for vault_service.py"""
    
    def test_get_vault_secret_not_found(self):
        """Test get_vault_secret when secret doesn't exist."""
        from server_shared.vault_service import get_vault_secret
        
        with patch('anvil.tables.app_tables.vault.find_one') as mock_find:
            mock_find.return_value = None
            
            with pytest.raises(VaultSecretNotFoundError) as exc_info:
                get_vault_secret("nonexistent_secret")
            
            assert "not configured" in str(exc_info.value)
    
    @patch('anvil.tables.app_tables.vault.find_one')
    @patch('server_shared.vault_service.decrypt')
    def test_get_vault_secret_success(self, mock_decrypt, mock_find):
        """Test successful vault secret retrieval."""
        from server_shared.vault_service import get_vault_secret
        
        mock_row = Mock()
        mock_row.value = "encrypted_value"
        mock_find.return_value = mock_row
        mock_decrypt.return_value = "decrypted_secret"
        
        result = get_vault_secret("stripe_secret_key")
        
        assert result == "decrypted_secret"
        mock_find.assert_called_once_with(name="stripe_secret_key")
        mock_decrypt.assert_called_once_with("encrypted_value")
    
    @patch('anvil.tables.app_tables.vault.find_one')
    @patch('server_shared.vault_service.decrypt')
    def test_get_vault_secret_decryption_error(self, mock_decrypt, mock_find):
        """Test vault secret retrieval when decryption fails."""
        from server_shared.vault_service import get_vault_secret
        
        mock_row = Mock()
        mock_row.value = "encrypted_value"
        mock_find.return_value = mock_row
        mock_decrypt.side_effect = VaultDecryptionError("Decryption failed")
        
        with pytest.raises(VaultDecryptionError):
            get_vault_secret("stripe_secret_key")
    
    @patch('anvil.tables.app_tables.vault.find_one')
    def test_get_vault_secret_general_exception(self, mock_find):
        """Test vault secret retrieval handles general exceptions gracefully."""
        from server_shared.vault_service import get_vault_secret
        
        mock_row = Mock()
        mock_row.value = "encrypted_value"
        mock_find.return_value = mock_row
        
        with patch('server_shared.vault_service.decrypt', side_effect=Exception("Unknown error")):
            with pytest.raises(VaultSecretNotFoundError) as exc_info:
                get_vault_secret("stripe_secret_key")
            
            assert "Contact support" in str(exc_info.value)
