# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params
from utilities.open_source.modules import import_run_user_only

def run():
    Params.setCalculated('scenario_section', __package__.split('.')[-1])
    run_user_only()
    Params.setParam(None, 'phase_reporting', '1')
    return

def run_user_only():
    import_run_user_only('..\\..\\..\\..\\..\\br_ashu_hobl\\HOBL_MINCP\\scenarios\\macos\\_library\\productivity\\prod_word_open', here=__file__)
    import_run_user_only('scenarios\\macos\\_library\\productivity\\mac_prod_run')
    import_run_user_only('scenarios\\macos\\_library\\productivity\\prod_XL_open_code')
    import_run_user_only('scenarios\\macos\\_library\\productivity\\prod_close')
    import_run_user_only('scenarios\\macos\\_library\\productivity\\prod_excel_close')
    import_run_user_only('scenarios\\macos\\_library\\productivity\\prod_excel_open')
    import_run_user_only('scenarios\\macos\\_library\\productivity\\prod_excel_run')
    import_run_user_only('scenarios\\macos\\_library\\productivity\\prod_kill')
    import_run_user_only('scenarios\\macos\\_library\\productivity\\prod_open')
    import_run_user_only('scenarios\\macos\\_library\\productivity\\prod_setup')
    return
