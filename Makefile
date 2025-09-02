up:
\tdocker compose up -d --build

down:
\tdocker compose down

logs:
\tdocker compose logs -f --tail=100

ps:
\tdocker compose ps

backup:
\tdocker compose exec db sh -c 'pg_dump -U $$POSTGRES_USER $$POSTGRES_DB > /backups/backup_$$(date +%F_%H-%M).sql'

restore FILE?=backups/backup.sql
restore:
\tdocker compose exec -T db sh -c 'psql -U $$POSTGRES_USER $$POSTGRES_DB < /$(FILE)'
