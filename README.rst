Django Introduction
*******************

Django Introduction is set of slides to educate more people about Django.

It was made with `reveal.js`_ and Raphaël_ and should work in all modern
browsers, even on tablets and smartphones.

The layout has been optimized for a resolution of 1024x768 pixels.

You can export it as PDF by using Chrome's print function, but there is
a problem with the charts.

English and German slides are available at http://www.django-introduction.com/

.. _reveal.js: https://github.com/hakimel/reveal.js/
.. _Raphaël: http://raphaeljs.com/

How to get django-introduction
==============================

Clone the repository::

    $ hg clone https://bitbucket.org/keimlink/django-introduction

You will need Mercurial_ and Git_ because reveal.js is included as a
Git subrepository.

Modify the slides as you like.

.. _Mercurial: http://mercurial.selenic.com/
.. _Git: http://git-scm.com/

How to create a static distribution and deploy it
=================================================

To create a static version for redistribution use the following command::

    $ make static

To serve the static files using a local webserver run the ``serve`` command::

    $ make serve

You can also use Fabric_ to deploy the static files on your server. If
Fabric is not installed on your machine run first::

    $ pip install fabric

Then deploy the static files on your server using Fabric::

    $ fab deploy:/path/where/static/files/go

If you want to make deployment with Fabric easy repeatable you can use a
``fabricrc`` file like this::

    user = alice
    host_string = slides.example.com
    remotepath = /path/where/static/files/go

And then use it like so::

    $ fab -c fabricrc deploy

.. _Fabric: http://fabfile.org/

Contributions and Bugs
======================

Feel free to improve django-introduction or create translations. `Pull
requests are welcome!`_

If you find a bug or have ideas for improvements use the `issue tracker`_.

.. _Pull requests are welcome!: https://bitbucket.org/keimlink/django-introduction
.. _issue tracker: https://bitbucket.org/keimlink/django-introduction/issues?status=new&status=open

License
=======

This work is licensed under the `Creative Commons Attribution-ShareAlike
3.0 Unported License <http://creativecommons.org/licenses/by-sa/3.0/>`_.

The JavaScript code to render the SVG charts is licensed under the New
BSD License.
