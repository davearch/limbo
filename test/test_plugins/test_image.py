# -*- coding: UTF-8 -*-
import os
import sys

from nose.tools import eq_
import vcr

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(DIR, '../../limbo/plugins'))

from image import on_message, unescape

# The set of valid images given the bananas fixture
bananas_images = [u'http://cdn1.medicalnewstoday.com/content/images/articles/271157-bananas.jpg', u'http://runhaven.com/wp-content/uploads/minion-bananas.jpg', u'https://www.organicfacts.net/wp-content/uploads/2013/05/Banana21.jpg', u'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Bananas.jpg/1024px-Bananas.jpg', u'http://dreamatico.com/data_images/banana/banana-3.jpg', u'http://www.esbtrib.com/wp-content/uploads/2015/09/bananas1.jpeg', u'http://weknowyourdreams.com/images/banana/banana-07.jpg', u'http://saltmarshrunning.com/wp-content/uploads/2014/09/bananasf.jpg', u'https://www.organicfacts.net/wp-content/uploads/2013/05/Banana3.jpg', u'http://bed56888308e93972c04-0dfc23b7b97881dee012a129d9518bae.r34.cf1.rackcdn.com/sites/default/files/imagecache/310_square/bananas_1.jpg', u'http://www.fitnessworksmb.com/wp-content/uploads/banana.jpg', u'https://media.licdn.com/mpr/mpr/shrinknp_800_800/AAEAAQAAAAAAAARXAAAAJGU2NGE1NzUzLTgxNzYtNDZiZC05YWY1LWQ4ZWE0OTk0NDY2Mw.jpg', u'https://charinacabswords.files.wordpress.com/2015/07/health-benefits-of-bananas.jpg', u'http://www.unitedfreshservices.com/content/01-services_bananen_rijperij/banana_ripening.jpg', u'http://parentinghealthybabies.com/wp-content/uploads/2013/03/bananas.jpg', u'http://foodmatters.tv/images/bananas.jpg', u'http://a3145z3.americdn.com/wp-content/uploads/2014/03/10-amazing-facts-bananas.jpg', u'http://www.popsci.com/sites/popsci.com/files/styles/large_1x_/public/import/2014/bananas-flickr-ian-ransley-design-dog-ccby20.jpg?itok%754G6KHch5', u'http://nobacks.com/wp-content/uploads/2014/11/Banana-21.png', u'http://i.telegraph.co.uk/multimedia/archive/01423/banana_1423728c.jpg']

def test_image():
    with vcr.use_cassette('test/fixtures/image_bananas.yaml'):
        ret = on_message({"text": u"!image bananas"}, None)
        assert ret in bananas_images, "{0} not in {1}".format(ret, bananas_images)

def test_unicode():
    with vcr.use_cassette('test/fixtures/image_unicode.yaml'):
        ret = on_message({"text": u"!image Mötörhead"}, None)
        # not blowing up == success, for our purposes
