.PHONY: deploy teardown run log help

help:
	@echo "Usage:"
	@echo "  make deploy            Redeploy the function"
	@echo "  make teardown          Tear down the function"
	@echo "  make env               Print the environment variables"
	@echo "  make log [N]           Show the last N lines of function logs (default 20)"
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

log:
	@echo "Showing function logs..."
	./log.sh $(N)
	@echo "Done showing function logs."
