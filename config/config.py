import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ruta al archivo de configuración
base_dir = os.path.dirname(os.path.abspath(__file__))
config_path_exp = os.path.join(base_dir, "./conf_global/app-config-exp.json")
