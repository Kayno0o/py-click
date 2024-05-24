setup:
	./generate_service.sh
	mkdir reports
	ln -s ./reports ~/reports
	sudo cp clicklog.python.service /etc/systemd/system/clicklog.python.service
	sudo systemctl enable --now clicklog.python.service

update:
	git pull
	./generate_service.sh
	mkdir reports || true
	ln -s ./reports ~/reports || true
	sudo cp clicklog.python.service /etc/systemd/system/clicklog.python.service
	sudo systemctl daemon-reload
	sudo systemctl restart clicklog.python.service

stop:
	sudo systemctl stop clicklog.python.service
