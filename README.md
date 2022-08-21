This repository contains several proof-of-concept GitHub Actions workflows.

1. `download-artifact.yml`

Download an artifact previously uploaded by another job by `run_id` and `name`.

2. `input-list.yml`

Input a JSON array and use it to set up a matrix to run multiple jobs.

3. `input-matrix.yml`

Input a JSON document which becomes the content of `jobs.<job_id>.strategy.matrix`.

4. `migrate-db.yml`

Use a custom action `xueke477/flyway-migration` to migrate MySQL database using `Flyway`.

5. `sam-build.yml`

Use `sam build -u` to build Zip deployment packages for AWS Lambda.

6. `sceptre-deploy.yml`

Deploy AWS CloudFormation stacks using `sceptre`.

7. `unit-test.yml`

Set up unit tests using `poetry` and run them with `pytest`.
