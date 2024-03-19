# setup

```bash
sudo cp clicklog.python.service /etc/systemd/system/clicklog.python.service
sudo systemctl enable --now clicklog.python.service
```

# update

```bash
git pull
sudo cp clicklog.python.service /etc/systemd/system/clicklog.python.service
sudo systemctl restart clicklog.python.service
```
