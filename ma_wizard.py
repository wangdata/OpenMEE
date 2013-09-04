################
#              #
# George Dietz #
# CEBM@Brown   #
#              #
################

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *

from globals import *

from choose_effect_size_page import ChooseEffectSizePage
from data_location_page import DataLocationPage
from refine_studies_page import RefineStudiesPage
from methods_and_parameters_page import MethodsAndParametersPage
from subgroup_variable_page import SubgroupVariablePage
from select_covariates_page import SelectCovariatesPage

Page_ChooseEffectSize, Page_DataLocation, Page_RefineStudies, Page_MethodsAndParameters, Page_SubgroupVariable, Page_SelectCovariates = range(6)
class MetaAnalysisWizard(QtGui.QWizard):
    def __init__(self, model, meta_f_str=None, mode = MA_MODE, parent=None):
        super(MetaAnalysisWizard, self).__init__(parent)
        
        self.model = model
        self.meta_f_str = meta_f_str
        self.mode = mode
        
        self.selected_data_type = None
        self.selected_metric = None
        self.data_location = None
        self.studies_included_table = None # dict mapping studies to if their inclusion state
        self.subgroup_variable_column = None
        self.covariates_included_table = None
        self.using_fixed_effects = None # will be a callable returning a boolean
        self.get_confidence_level = None # will be a callable returning a double
        
        self.methods_and_params_page_instance = MethodsAndParametersPage(model=model, meta_f_str=meta_f_str)
        
        self.setPage(Page_ChooseEffectSize, ChooseEffectSizePage(add_generic_effect=True))
        self.setPage(Page_DataLocation,     DataLocationPage(model=model, mode=MA_MODE))
        
        self.setPage(Page_MethodsAndParameters, self.methods_and_params_page_instance)
        self.setPage(Page_RefineStudies,    RefineStudiesPage(model=model)) ###
        if mode==SUBGROUP_MODE:
            self.setPage(Page_SubgroupVariable, SubgroupVariablePage(model=model))
        elif mode==META_REG_MODE:
            self.setPage(Page_SelectCovariates, SelectCovariatesPage(model=model))
            self.setPage(Page_RefineStudies, RefineStudiesPage(model=model, mode=mode))
#        else:
#            self.setPage(Page_RefineStudies,    RefineStudiesPage(model=model))
        
        self.setStartId(Page_ChooseEffectSize)
        self.setWizardStyle(QWizard.ClassicStyle)
        

        
        QObject.connect(self, SIGNAL("currentIdChanged(int)"), self._change_size)
    
    def _change_size(self, pageid):
        print("changing size")
        self.adjustSize()
        
    def get_included_covariates(self):
        included_covariates = [cov for cov,should_include in self.covariates_included_table.iteritems() if should_include]
        return included_covariates
        
    def get_subgroup_variable_column(self):
        return self.subgroup_variable_column
    
    def get_subgroup_variable(self):
        if self.subgroup_variable_column is None:
            return None
        return self.model.get_variable_assigned_to_column(self.subgroup_variable_column)
        
    def get_plot_params(self):
        return self.methods_and_params_page_instance.get_plot_params()
    
    def get_current_method(self):
        return self.methods_and_params_page_instance.get_current_method()
    
    def get_modified_meta_f_str(self):
        return self.methods_and_params_page_instance.get_modified_meta_f_str()
        
    def get_included_studies_in_proper_order(self):
        all_studies = self.model.get_studies_in_current_order()
        included_studies = [study for study in all_studies if self.studies_included_table[study]==True]
        return included_studies


    def nextId(self):
        if self.mode==SUBGROUP_MODE:
            # this is redundant but it makes the path easier to understand
            if self.currentId() == Page_ChooseEffectSize:
                return Page_DataLocation
            elif self.currentId() == Page_DataLocation:
                return Page_RefineStudies
            elif self.currentId() == Page_RefineStudies:
                return Page_SubgroupVariable
            elif self.currentId() == Page_SubgroupVariable:  #
                return Page_MethodsAndParameters             #
            elif self.currentId() == Page_MethodsAndParameters:
                return -1
        elif self.mode == META_REG_MODE:
            if self.currentId() == Page_ChooseEffectSize:
                return Page_DataLocation
            elif self.currentId() == Page_DataLocation:
                return Page_SelectCovariates
            elif self.currentId() == Page_SelectCovariates:
                return Page_RefineStudies
            elif self.currentId() == Page_RefineStudies:
                return -1
        else:
            if self.currentId() == Page_ChooseEffectSize:
                return Page_DataLocation
            elif self.currentId() == Page_DataLocation:
                return Page_RefineStudies
            elif self.currentId() == Page_RefineStudies:
                return Page_MethodsAndParameters
            elif self.currentId() == Page_MethodsAndParameters:
                return -1
        

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    wizard = MetaAnalysisWizard(parent=None)
    wizard.show()
    sys.exit(app.exec_())