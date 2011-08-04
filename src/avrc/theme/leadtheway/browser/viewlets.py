from five import grok
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from plone.app.layout.viewlets.interfaces import IPortalHeader
from zope.interface import Interface
from zope.app.component.hooks import getSite
import random
# Apply on everything.
# Use templates directory to search for templates.
from Products.CMFCore.utils import getToolByName

grok.templatedir('templates')

class SlideshowViewlet(grok.Viewlet):
    grok.name('leadtheway.SlideshowViewlet')
    grok.context(Interface)
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader)

    
    def slideshowImages(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        portal_url = getToolByName(self.context, "portal_url")
        slideshow_path = portal_url.getPortalPath() + '/slideshow'
        imageBrains = list(catalog({'portal_type':'Image','path':slideshow_path}))
        random.shuffle(imageBrains)
        return imageBrains
