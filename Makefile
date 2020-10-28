# use bash
CURR_DIR		:=	$(shell pwd)
NEW_TAG			=	$(shell date +"%Y%m%d%H%M")
LATEST_IMGID	= 	$(shell docker images weekly-report-builder -q)

.PHONY: all install-pippkg update-pippkg run run_in_container run_grubber test build_image push_image

all:

install-pippkg:
	pip install -r requirements.txt

update-pippkg:
	pipenv sync
	pipenv run pip freeze > requirements.txt

run:
	python app.py

run_in_container:
	make run

run_grab_sheet:
	[ ! -d news ] && mkdir news && echo "Generate news dir" || echo "News Dir existed"
	docker run -it --rm -v "${CURR_DIR}"/news:/source/news news-grabber

run_grab_all:
	[ ! -d news ] && mkdir news && echo "Generate news dir" || echo "News Dir existed"
	docker run -it --rm -v "${CURR_DIR}"/news:/source/news news-grabber python app.py -tlq

test:
	echo ${CURR_DIR}

build_image:
	# docker rmi -f ${LATEST_IMGID}
	make update-pippkg
	docker build -t news-grabber . --no-cache

push_image:
	docker tag news-grabber:latest nipapa/news-grabber:latest
	docker tag news-grabber:latest nipapa/news-grabber:${NEW_TAG}
	# docker push nipapa/news-grabber:latest
	# docker push nipapa/news-grabber:${NEW_TAG}
	# aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 522073198850.dkr.ecr.ap-northeast-1.amazonaws.com
	docker tag news-grabber:latest 522073198850.dkr.ecr.ap-northeast-1.amazonaws.com/news-grabber:latest
	docker tag news-grabber:latest 522073198850.dkr.ecr.ap-northeast-1.amazonaws.com/news-grabber:${NEW_TAG}
	docker push 522073198850.dkr.ecr.ap-northeast-1.amazonaws.com/news-grabber:latest
	docker push 522073198850.dkr.ecr.ap-northeast-1.amazonaws.com/news-grabber:${NEW_TAG}
