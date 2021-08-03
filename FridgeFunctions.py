##############################################################
# Home to any and all function declarations for this project #
##############################################################
def recursive_find_tab_by_id(self,key,topwidget):
    for widget in topwidget.children:
        try:
            if widget.id == key:
                return widget
            else:
                w = recursive_find_tab_by_id(self,key,widget)
                if w is not None:
                    return w
        except AttributeError as e:
            pass
