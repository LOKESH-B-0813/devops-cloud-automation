# env_var_auditor.py - Inspects critical system environment paths
import os
print(f"Shell Path: {os.environ.get('SHELL', 'Unknown')}")
print(f"User: {os.environ.get('USER', 'Unknown')}")
