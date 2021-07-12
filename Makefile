do-report:
	./scripts/report.py videos/*.json | tail -6 > /tmp/report.md
