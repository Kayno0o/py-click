setup:
	./generate_service.sh
	sudo cp clicklog.python.service /etc/systemd/system/clicklog.python.service
	sudo systemctl enable --now clicklog.python.service

update:
	git pull
	./generate_service.sh
	sudo cp clicklog.python.service /etc/systemd/system/clicklog.python.service
	sudo systemctl daemon-reload
	sudo systemctl restart clicklog.python.service
