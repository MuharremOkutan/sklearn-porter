# -*- coding: utf-8 -*-

import unittest

from sklearn.tree import DecisionTreeClassifier
from sklearn_porter import Porter

from ..CTest import CTest


class DecisionTreeClassifierTest(CTest, unittest.TestCase):

    def setUp(self):
        super(DecisionTreeClassifierTest, self).setUp()
        self.porter = Porter(language='c')
        self._port_model(DecisionTreeClassifier(random_state=0))

    def tearDown(self):
        super(DecisionTreeClassifierTest, self).tearDown()
