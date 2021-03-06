"""Testing setup providing layers and fixtures
TextIndexerLayer                   basic text indexer layer
TEXT_INDEXER_FIXTURE               text indexer fixture
TEXT_INTEXER_INTEGRATION_TESTING   integration testing layer
TEXT_INDEXER_FUNCTIONAL_TESTING    functional testing layer
"""

from StringIO import StringIO
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from zope.configuration import xmlconfig
import logging


class TextIndexerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def __init__(self, *args, **kwargs):
        super(TextIndexerLayer, self).__init__(*args, **kwargs)
        self.log = None
        self.log_handler = None

    def setUpZope(self, app, configurationContext):
        """After setting up zope, load all necessary zcml files.
        """
        import collective.dexteritytextindexer
        xmlconfig.file('configure.zcml', collective.dexteritytextindexer,
                       context=configurationContext)
        import collective.dexteritytextindexer.tests
        xmlconfig.file('configure.zcml',
                       collective.dexteritytextindexer.tests,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        """After setting up plone, give Manager role to the test user.
        """
        setRoles(portal, TEST_USER_ID, ['Manager'])

    def testSetUp(self):
        super(TextIndexerLayer, self).testSetUp()
        self.log = StringIO()
        self.log_handler = logging.StreamHandler(self.log)
        logging.root.addHandler(self.log_handler)
        self['read_log'] = self.read_log

    def testTearDown(self):
        super(TextIndexerLayer, self).testTearDown()
        logging.root.removeHandler(self.log_handler)

    def read_log(self):
        self.log.seek(0)
        return self.log.read().strip()


TEXT_INDEXER_FIXTURE = TextIndexerLayer()
TEXT_INTEXER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TEXT_INDEXER_FIXTURE,),
    name="collective.dexteritytextindexer:Integration")


class TextIndexerFunctionalLayer(PloneSandboxLayer):

    defaultBases = (TEXT_INDEXER_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import plone.app.dexterity
        xmlconfig.file('configure.zcml', plone.app.dexterity,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'plone.app.dexterity:default')

TEXT_INDEXER_FUNCTIONAL_FIXTURE = TextIndexerFunctionalLayer()

TEXT_INDEXER_FUNCTIONAL_TESTING = FunctionalTesting(
        bases=(TEXT_INDEXER_FUNCTIONAL_FIXTURE,),
        name="collective.dexteritytextindexer:Functional")
