Enable

1. Move xmas_tree.service to /etc/systemd/system/
2. Run command 'sudo chmod +x xmas_main.py' to enable it to be executed
3. Enable service 'sudo systemctl start xmas_tree.service'
4. Run service at boot 'sudo systemctl enable xmas_tree.service'

Disable it running

1. 'sudo systemctl stop xmas_tree.service'
2. 'sudo systemctl disable xmas_tree.service'
