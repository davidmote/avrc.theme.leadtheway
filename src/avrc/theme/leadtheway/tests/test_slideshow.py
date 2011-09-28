import unittest2 as unittest

from plone.testing.z2 import Browser
from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, TEST_USER_PASSWORD
from plone.app.testing import setRoles
import transaction; 
from avrc.theme.leadtheway.testing import LEADTHEWAY_THEME_INTEGRATION_TESTING, LEADTHEWAY_THEME_FUNCTIONAL_TESTING

## This is how you get a viewlet 
#        viewlet = ViewletName(context, request, None, None)

class TestViewlet(unittest.TestCase):
    layer= LEADTHEWAY_THEME_INTEGRATION_TESTING
    
    def setUp(self):
        from avrc.theme.leadtheway.browser.viewlets import SlideshowViewlet
        portal = self.layer['portal']
        request = self.layer['request']
        self.homepage_viewlet = SlideshowViewlet(portal, request, None, None)
        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory('Document', 'page', title=u"Page 1")
        setRoles(portal, TEST_USER_ID, ['Anonymous'])
        self.subpage_viewlet = SlideshowViewlet(portal['page'], request, None, None)
    
    def tearDown(self):
        portal = self.layer['portal']
        del self.homepage_viewlet
        del self.subpage_viewlet
        del portal['page']
            
    def test_viewlet_container(self):
        portal = self.layer['portal']
        self.assertEquals(None, self.homepage_viewlet.slideshowContainer())
        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory('Folder', 'slideshow')
        setRoles(portal, TEST_USER_ID, ['Anonymous'])
        self.assertEquals(portal.restrictedTraverse('slideshow'), self.homepage_viewlet.slideshowContainer())

    def test_home_check(self):
        self.assertTrue(self.homepage_viewlet.isHomePage())
        self.assertFalse(self.subpage_viewlet.isHomePage())

    def test_slideshow_images(self):
        ## We will need a slideshow container
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory('Folder', 'slideshow')
        slideshow_container = portal['slideshow']
        for img in ['1.png','2.png', '3.png']:
            slideshow_container.invokeFactory('Image', img)
        setRoles(portal, TEST_USER_ID, ['Anonymous'])
        self.assertEqual(3, len(self.homepage_viewlet.slideshowImages()))
        del portal['slideshow']

        
    def test_mosaic_images(self):
        portal = self.layer['portal']
        imagelist = self.subpage_viewlet.mosaicImages()
        self.assertEqual(16, len(imagelist))

class TestSlideshowViewlet(unittest.TestCase):

    layer = LEADTHEWAY_THEME_FUNCTIONAL_TESTING

    def setUp(self):
        from avrc.theme.leadtheway.browser.viewlets import SlideshowViewlet
        portal = self.layer['portal']
        request = self.layer['request']
        self.homepage_viewlet = SlideshowViewlet(portal, request, None, None)
        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory('Document', 'page', title=u"Page 1")
        portal.invokeFactory('Folder', 'slideshow')
        slideshow_container=portal['slideshow']
        for img in ['slideshow01.png','slideshow02.png', 'slideshow03.png']:
            slideshow_container.invokeFactory('Image', img)
        transaction.commit()
        setRoles(portal, TEST_USER_ID, ['Anonymous'])
        self.subpage_viewlet = SlideshowViewlet(portal['page'], request, None, None)
    
    def tearDown(self):
        portal = self.layer['portal']
        del self.homepage_viewlet
        del self.subpage_viewlet
        del portal['page']
        del portal['slideshow']
        transaction.commit()
    def test_render_homepage_slideshow(self):
        app = self.layer['app']
        portal = self.layer['portal']
        
        browser = Browser(app)
        browser.handleErrors = False
        
        # Render the cinema
        browser.open(portal.absolute_url())
        self.assertTrue('slideshow01.png' in browser.contents)
        self.assertFalse('mosaic01.png' in browser.contents)

    def test_render_subpage_slideshow(self):
        app = self.layer['app']
        portal = self.layer['portal']
        
        browser = Browser(app)
        browser.handleErrors = False
        # Render the cinema
        browser.open(portal.absolute_url()+'/page')
        self.assertFalse('slideshow01.png' in browser.contents)
        self.assertTrue('mosaic01.png' in browser.contents)