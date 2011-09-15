from five import grok
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from plone.app.layout.viewlets.interfaces import IPortalHeader
from zope.interface import Interface
from zope.app.component.hooks import getSite
import random
# Apply on everything.
# Use templates directory to search for templates.
grok.templatedir('templates')

class SlideshowViewlet(grok.Viewlet):
    grok.name('leadtheway.SlideshowViewlet')
    grok.context(Interface)
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader)

    
    def slideshowContainer(self):
        site = getSite()
        try:
            return site.restrictedTraverse('slideshow')
        except KeyError:
            return None

    def isHomePage(self):
        return self.context.restrictedTraverse('@@plone_context_state').is_portal_root()
        
    def slideshowImages(self):
        slideshow_container = self.slideshowContainer()
        if slideshow_container is not None:
            imageBrains = list(slideshow_container.getFolderContents({'portal_type':'Image'}))
            random.shuffle(imageBrains)
        else:
            imageBrains = []
        return imageBrains
        
        
    def mosaicImages(self):
        theme_path = '++theme++avrc.theme.leadtheway/theme-mosaic'
        theme_dir = self.context.restrictedTraverse(theme_path)
        rslts = []
        for image in theme_dir.listDirectory():
            rslts.append(theme_path + '/' + image)
        return rslts