# CompleteFramework

* Apk tested:

        SauceLabs Apk

* To create virtual environment called "venv":

        virtualenv env

* To enter virtual environment called "venv":

        source venv/Scripts/activate

* To quit virtual environment (first we have to be on the virtual environment):

        deactivate

* To delete virtual environment called "venv":

        rm -r venv/

* To install requirements in the virtual env:

        source venv/Scripts/activate
        pip install -r requirements.txt

* Run on commandline:

       pytest -m ${tag_name} --device_name=${device_name}

* Example:

        pytest -m regression --browser=edge

*if no device name specified it will take mobile_emulator by default*

* To see allure results:

        allure serve resources/reports/my-allure-results/

* Jenkins shell script:

        virtualenv venv
        source venv/bin/activate
        pip install -r requirements.txt
        pytest -m ${group} --os_version="${os_version}" --device_name="${device_name}"
        deactivate
