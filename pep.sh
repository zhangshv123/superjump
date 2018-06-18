function check(){
	pep8 --show-source --show-pep8 $1
	pylint $1
}

function checkJava(){
	java -jar lib/checkstyle-7.1.1-all.jar -c lib/sun_checks.xml $argv
	java -jar lib/checkstyle-7.1.1-all.jar -c lib/google_checks.xml $argv
}
#checkJava hard/LC358.java
#
java -jar lib/checkstyle-7.1.1-all.jar -c lib/sun_checks.xml hard/LC358.java