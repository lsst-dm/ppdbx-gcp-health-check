help:
	@echo "Usage:"
	@echo "  make deploy            Redeploy the function"
	@echo "  make teardown          Tear down the function"
	@echo "  make env               Print the environment variables"
	@echo "  make help              Show this help message"

deploy:
	@echo "Deploying function..."
	./deploy.sh
	@echo "Done deploying function."

teardown:
	@echo "Tearing down function..."
	./teardown.sh
	@echo "Done tearing down function."

run:
	@echo "Running function..."
	./run.sh
	@echo "Done running function."
