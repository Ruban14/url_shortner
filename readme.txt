scope:
    Inputing the Long URL and then the system should convert it to short url and then stored in the localfile.and
    then when again that same long url is provided , it should check with the local file and return the already
    created one.For this a UI for inputing the long url and viewing the output should be available and must be
    in docker image.

Steps to run the software

1. Create a virtualenv
    >>> python3 -m venv virtualenv

2. Activate the environment
    >>> source /virtualenv/bin/Activate
    (IF IT IS ACTIVATED THE NAME OF THE VIRTUALENV WILL BE DISPLAYED IN THE BEGGINIG OF THE LINE)

3. Install all the required packages inside the created virutalenv
    >>> pip install -r requirements

4. run the server
    >>> python manage.py runserver 0:8000

5. go to the browser
    a. go to url for inputing the long url: http://localhost:8000/urlApp/
    b. after providing the url press "Generate URL"
    c. It will navigate to the output page with the short url and there will be a option to copy the result URL

6. Inorder to give the URL from the API call
    a. go to the link : http://localhost:8000/urlApp/serve/shortned/url
    b. then input the post data inside that json part
        E.g: {"url": "https://www.youtube.com/playlist"}
    c. click submit and it will return you the short url.

7. all the docker based files are already inside the project directory.
