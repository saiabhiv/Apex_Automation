# coding: utf-8
#
# Copyright © 2022 Hexagon Manufacturing Intelligence, Inc. (“Hexagon”)
#  
# Permission to use Scripts
#  
# Permission is granted to customers of Hexagon and its affiliates with valid licenses of the MSC Apex™ software 
# to use script files posted on this page (collectively “Scripts”) solely for customers’ own authorized 
# internal use in conjunction with licensed use of the MSC Apex software.  
# No other use is permitted.  No license to MSC Apex or other software is granted under this Permission.
#  
# SCRIPTS ARE PROVIDED ON AN "AS-IS" BASIS, WITH NO WARRANTIES OF ANY KIND.  USE OF THE SCRIPTS IS AT CUSTOMER'S SOLE RISK.
#  
# IN NO EVENT SHALL HEXAGON, ITS AFFILIATES, SUBSIDIARIES, SUPPLIERS, AGENTS, REPRESENTATIVES OR EMPLOYEES BE LIABLE FOR ANY 
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL OR CONSEQUENTIAL DAMAGES HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, TORT, 
# STRICT LIABILITY, OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION USE OF THE SCRIPTS, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  
#  
# Customer shall indemnify, defend and hold Hexagon, its affiliates, subsidiaries, suppliers, agents, 
# employees or representatives (collectively, “Indemnified Parties”) harmless from and against any third-party claims 
# brought against Indemnified Parties rising out of or in connection with Customer’s use of the Scripts.
#
#
# Macro Name = aircraftIso1View
# 
# Macro Description = 
# 
# Macro Hot Key = 7
# 

import apex


apex.disableShowOutput()

myCamera = apex.display.getCamera()

myCamera.viewIsometric_4(reverse=False, viewUp = [0.0, 0.0, 1.0])

#myCamera.setViewUp(apex.construct.Vector3D(0.0, 0.0, 1.0))
#myCamera.reset()
