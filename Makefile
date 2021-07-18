.PHONY: redo-readme
redo-readme: do-report
	cat README.md | awk '{print} (NF==2 && $$1 == "##" && $$2 == "Status") {exit}' > /tmp/header.md
	cat README.md | awk 'BEGIN{ok=0} (NF==2 && $$1 == "##" && $$2 == "Methodology") {ok=1} ok==1 {print}' > /tmp/footer.md
	tail -7 /tmp/report.md > /tmp/middle.md
	echo > /tmp/empty.md
	cat /tmp/header.md /tmp/empty.md /tmp/middle.md /tmp/empty.md /tmp/footer.md > README.md

.PHONY: do-report
do-report:
	./scripts/report.py videos/*.json > /tmp/report.md
