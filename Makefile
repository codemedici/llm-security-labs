up:
	docker compose --file shared/docker/docker-compose.yml up --build

flag:
	curl -X POST -d "flag=$(flag)" http://localhost:1337/submit
# Auto-generated lab targets
lab-01:
	cd labs/01_prompt_injection && jupyter notebook

lab-02:
	cd labs/02_jailbreak && jupyter notebook

lab-03:
	cd labs/03_vector_poison && jupyter notebook

lab-04:
	cd labs/04_insecure_output && jupyter notebook

lab-05:
	cd labs/05_data_extraction && jupyter notebook

lab-06:
	cd labs/06_training_data_poisoning && jupyter notebook

lab-07:
	cd labs/07_adversarial_evasion && jupyter notebook

lab-08:
	cd labs/08_insecure_plugins && jupyter notebook

lab-09:
	cd labs/09_excessive_agency && jupyter notebook

lab-10:
	cd labs/10_model_manipulation && jupyter notebook

