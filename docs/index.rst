.. Navigating the Dark Web documentation master file, created by
   sphinx-quickstart on Mon Mar 24 18:18:19 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. meta::
	:description lang=en:
		“Navigating the Dark Web: A Comprehensive Guide to Darknets, Tools, and Intelligence” is an online book written by Sébastien Damaye. This book explains what the Dark Web is, how to access it, what content to expect, how to monitor the Dark Web and why it matters. I wrote this book to address many questions people have, to demystify the Dark Web, and share my experience with others.
	:google-site-verification: yAFBRXv6J0QsJeTI4nGlowCKX7m3dyaYFBMOmFHJN-I
	:msvalidate.01: D8E7042FD25E42708394BDF2529FFFCF

.. image:: images/bannerBackgroundImage.png

Welcome
=======

What Is It?
***********
"Navigating the Dark Web: A Comprehensive Guide to Darknets, Tools, and Intelligence" is an online book written by Sébastien Damaye. It is exclusively hosted online so that everybody can enjoy it for free, but you are very welcome to `support the author <#id1>`_.

This book explains what the Dark Web is, how to access it, what content to expect, how to monitor the Dark Web and why it matters. I wrote this book to address many questions people have, to demystify the Dark Web, and share my experience with others.

Why an Online Book?
*******************
I was initially planning to publish this book on Amazon. However the writing process took me more than two years, and I kept coming back to previous chapters to ensure that the content was always up to date (project names, versions, etc.).

I began to think that an online book would be a better place, especially because each reader could become a contributor (using the **Suggest edit** or **Open issue** buttons).

An online version can contain hyperlinks that redirect to other parts of the book, making the reading process much more interactive.

Besides, this book contains many links, code extracts and command lines that you can copy with a simple click.

And because all the content is indexed, searching for a particular term is also much easier online.

About the Author
****************
`Sébastien Damaye <https://www.linkedin.com/in/sebastiendamaye/>`_ is a cybersecurity expert with over 20 years of experience. He is known for his contributions to the field of cybersecurity, particularly in areas related to threat hunting and security tools.

Main contributions:

- https://www.aldeid.com/
- https://deephunter.readthedocs.io
- https://sourceforge.net/projects/pytbull/
- https://github.com/sebastiendamaye

Send the author an `email <https://spamty.eu/show/v6/11513/QovA91huoP7d2fe196v4migr/>`_.

Acknowledgments and Dedication
******************************
This book wouldn't exist without the incredible people who stood by me through every step of the journey.

To my friends and colleagues, thank you for your encouragement, thoughtful feedback, and reminders to keep going when motivation was slowing down. Your support meant a lot to me.

To my family, thank you for your patience, your love, and your quiet support. Whether it was giving me space to write or simply understanding when I disappeared into my head for a while, your presence made all the difference.

I'd like to dedicate this book to my brother, who died unexpectedly in the middle of writing this book.

Naming conventions
******************
In this book, we use specific text formatting to indicate different types of actions. Below are the conventions used:

.. list-table::
   :header-rows: 1

   * - Action
     - Example
   * - Select an option from a menu
     - In Google Chrome, go to **Settings > Privacy and security > Delete browing data**.
   * - Click a button or link
     - To start the installation, click **Next**.
   * - File names
     - Edit the ``settings.py`` file as shown below.
   * - Command line (dedicated block)
     - You can install Tor from the packages with the below command:

       .. code-block:: bash

            $ sudo apt update && sudo apt install tor
   * - Command to execute from a python virtual environment
     - 
       .. code-block:: bash

            (venv) $ pip install -r requirements.txt
   * - Code to adapt to your environment
     - Add ``127.0.0.1`` in the ``/etc/apache2/ports.conf`` file as shown below:

       .. code-block::
	        :emphasize-lines: 1,3,6
	        :caption: ``/etc/apache2/ports.conf``
			
	        Listen 127.0.0.1:80
	        <IfModule ssl_module>
		      Listen 127.0.0.1:443
	        </IfModule>
	        <IfModule mod_gnutls.c>
		      Listen 127.0.0.1:443
	        </IfModule>
   * - Command line (inline)
     - You can install Tor from the packages (``sudo apt update && sudo apt install tor``) or download the Tor Browser.
   * - Command output
     - The above command will produce a result similar to this:

	   16:72C351A6A2B3346260F62EACE3FF5C2D3FC283726E805141D1977B0C88

Support the Author
******************
This book is free for everyone to enjoy — no paywalls, no subscriptions, just shared with love. If you’ve found value in it and would like to support my work, you’re welcome to leave a donation.

There’s no pressure — your presence here already means a lot. But if you choose to contribute, know that it helps me keep this book updated.

Thank you for reading, and for being part of this journey.

.. image:: images/donate.png
	:target: https://www.paypal.com/donate?hosted_button_id=73UNLMZ6CC8C6
	:alt: support the author
	:width: 300

-----

.. toctree::
   :maxdepth: 4
   :Caption: Contents:
   
   foreword
   chapter1_overview_of_the_darkweb
   chapter2_tor
   chapter3_i2p
   chapter4_hyphanet
   chapter5_zeronet
   chapter6_what_can_be_found_on_the_darkweb
   chapter7_intelligence_and_hunting_on_the_darkweb
