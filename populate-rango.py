import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page
def populate():
    ml_pages=[{"title": "ML Wikipedia",
        "url":"https://en.wikipedia.org/wiki/Machine_learning"},
              {"title": "ML GFG",
               "url": "https://www.geeksforgeeks.org/machine-learning/"}
              ]
    kubernetes_pages = [{"title": "K8 official",
                 "url": "https://kubernetes.io/"},
                {"title": "Google K8 engine",
                 "url": "https://cloud.google.com/kubernetes-engine"}
                ]
    python_pages = [
        {"title": "Official Python Tutorial",
        "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
        "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
        "url":"http://www.korokithakis.net/tutorials/python/"} ]
    django_pages = [
        {"title":"Official Django Tutorial",
        "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks",
        "url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django",
        "url":"http://www.tangowithdjango.com/"} ]
    other_pages = [
        {"title":"Bottle",
        "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask",
        "url":"http://flask.pocoo.org"} ]
    cats = {("Python",128,64): {"pages": python_pages},
            ("Django",64,32): {"pages": django_pages},
            ("Other Frameworks",32,16): {"pages": other_pages},
            ("ML",232,116): {"pages": ml_pages},
            ("K8",32,46): {"pages": kubernetes_pages}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views+5
    p.save()
    return p

def add_cat(item):
    c = Category.objects.get_or_create(name=item[0],views=item[1],likes=item[2])[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()