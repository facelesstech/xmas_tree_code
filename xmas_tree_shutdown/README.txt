1. Move pishutdown.service to /etc/systemd/system/
2. Run command 'sudo chmod +x pishutdown.py' to enable it to be executed
3. Enable service 'sudo systemctl start pishutdown.service'
4. Run service at boot 'sudo systemctl enable pishutdown.service'
