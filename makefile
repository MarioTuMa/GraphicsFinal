test: test.mdl main.py matrix.py mdl.py display.py draw.py gmath.py
	python3 fonts/genFont.py
	python3 fonts/getLetter.py
	python3 main.py test.mdl

clean:
	rm *pyc *out parsetab.py

clear:
	-rm *pyc -i
	-rm *out -i
	echo clearing your stuff
	-rm parsetab.py -i
	-rm *.ppm -i
	-rm *.png -i
	-rm anim/*.png -i
	-rm chars/*.ppm -i
	-rm *.gif -i
	-rm -rf __pycache__ -i
