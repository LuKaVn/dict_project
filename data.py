#Error messages for the complete inverter unit
'''
    "1" : {
        "discript" : " ",
        "cause": " ",
        "Measures" : " "
        } 
'''
IVT = {
    "1" : {
        "discript" : " Modbus TCP value out of range",
        "cause": " Possible causes The permissible range for data that has been transmited via the Modbus TCP interface is too small.",
        "Measures" : " Check the permissible range for data that are transmitted via the Modbus TCP interface."
        },
    "2" : {
        "discript" : "Configuration corrupt ",
        "cause": " Transmission of configuration data has failed ",
        "Measures" : "e.g. because of a defective USB flashdrive Measures Check the USB flashdrive."
        } ,
    "3" : {
        "discript" : "APU 1 / 2 cooling fluid low",
        "cause": " The filling level of the cooling liquid is too low. ",
        "Measures" : " • Check the filling level of the cooling liquid. If the filling level is the cooling liquid is too low, replenish the cooling liquid. • Open the doors in the cabinet +C3. • Check all pipes and hoses for leaks. If leaks are found, contact the manufacturer. You will find information on this in Chapter Technical support (page 355)."
        },
    "4" : {
        "discript" : "APU 3 / 4 cooling fluid low ",
        "cause": " The filling level of the cooling liquid is too low. ",
        "Measures" : " • Check the filling level of the cooling liquid. If the filling level is the cooling liquid is too low, replenish the cooling liquid. • Open the doors in the cabinet +C6. • Check all pipes and hoses for leaks. If leaks are found, contact the manufacturer. You will find information on this in Chapter Technical support (page 355)."
        } ,
    "5" : {
        "discript" : "No enable signal ",
        "cause": " The cabinet doors were open. ",
        "Measures" : " • Check whether the main switch is open. If the main switch is open, closed it. • Check whether all cabinet doors are closed. If the cabinet doors are open, close them."
        } ,
    "6" : {
        "discript" : " No supply voltage ",
        "cause": " There is a connection fault. ",
        "Measures" : " Check the connections for the power supply. "
        }, 
    "7" : {
        "discript" : " Medium voltage switch gear off ",
        "cause": " The medium-voltage switchgear is switched off. ",
        "Measures" : " The medium-voltage switchgear is switched on. "
        }, 
    "8" : {
        "discript" : " DI Temperature not OK ",
        "cause": " The temperature in the cabinet is too high. ",
        "Measures" : " • Switch the radial ventilation on manually via the remote access connection. • Check whether the radial ventilation is switched on."
        }, 
    "9" : {
        "discript" : " DI medium voltage transformer error ",
        "cause": " causes The medium-voltage transformer is faulty. ",
        "Measures" : " • Check the medium-voltage transformer for shortcircuits and internal faults. • Check the filling level of the insulation oil of the medium-voltage transformer. If the filling level is too low, contact the manufacturer. You will find information on this in Chapter Technical support (page 355). "
        }, 
    "10" : {
        "discript" : " APU 1 / 2 water pump switching cycles ",
        "cause": " The water pump switches on and off more than 60 times per hour.",
        "Measures" : " Check the control loop of the cooling system. "
        } , 
    "11" : {
        "discript" : " APU 3 / 4 water pump switching cycles ",
        "cause": " The water pump switches on and off more than 60 times per hour.",
        "Measures" : " Check the control loop of the cooling system. "
        }, 
    "12" : {
        "discript" : " APU 5 / 6 water pump switching cycles ",
        "cause": " ",
        "Measures" : " Check the control loop of the cooling system. "
        }, 
    "13" : {
        "discript" : " APU 1 / 2 air-to-air cooler switching cycles ",
        "cause": " The air-to-air heat exchanger switches on and off more than 60 times per hour.",
        "Measures" : " Check the control loop of the cooling system. "
        },
    "14" : {
        "discript" : " APU 3 / 4 air-to-air cooler switching cycles ",
        "cause": " The air-to-air heat exchanger switches on and off more than 60 times per hour.",
        "Measures" : " Check the control loop of the cooling system. "
        }, 
    "15" : {
        "discript" : " APU 5 / 6 air-to-air cooler switching cycles ",
        "cause": " The air-to-air heat exchanger switches on and off more than 60 times per hour.",
        "Measures" : " Check the control loop of the cooling system. "
        } ,
    "16" : {
        "discript" : " APU 1 / 2 water air cooler switching cycles ",
        "cause": " The water-to-air heat exchanger switches on and off more than 60 times per hour. ",
        "Measures" : " Check the control loop of the cooling system. "
        } ,
    "17" : {
        "discript" : " APU 3 / 4 water air cooler switching cycles ",
        "cause": " The water-to-air heat exchanger switches on and off more than 60 times per hour. ",
        "Measures" : " Check the control loop of the cooling system. "
        }, 
    "18" : {
        "discript" : " APU 5 / 6 water air cooler switching cycles ",
        "cause": " The water-to-air heat exchanger switches on and off more than 60 times per hour. ",
        "Measures" : " Check the control loop of the cooling system. "
        } ,
    "19" : {
        "discript" : "  Supply voltage low ",
        "cause": " The grid voltage is too low. ",
        "Measures" : " Check the grid voltage at terminal -TB1 in cabinet +C1. "
        }, 
    "20" : {
        "discript" : " Modbus TCP timeout ",
        "cause": " The Modbus TCP timeout is shorter than the time since the last network query. ",
        "Measures" : " • Check whether the Modbus TCP interface is functional. • Check whether the Modbus TCP timeout is correctly set. "
        } ,
    "21" : {
        "discript" : " APU 1 / 2 insulation ",
        "cause": " • The insulation monitor mode is set to 0. • The insulation monitor is faulty. ",
        "Measures" : "  • Check whether the insulation monitoring mode is correctly set. • Check the insulation monitor."
        } ,
    "22" : {
        "discript" : " APU 3 / 4 insulation ",
        "cause": " • The insulation monitor mode is set to 0. • The insulation monitor is faulty. ",
        "Measures" : "  • Check whether the insulation monitoring mode is correctly set. • Check the insulation monitor."
        }, 
    "23" : {
        "discript" : " APU 5 / 6 insulation ",
        "cause": " • The insulation monitor mode is set to 0. • The insulation monitor is faulty. ",
        "Measures" : " • Check whether the insulation monitoring mode is correctly set. • Check the insulation monitor."
        }, 
    "24" : {
        "discript" : " Medium voltage transformer temperature high ",
        "cause": " The temperature of the medium-voltage transformer is higher than permitted.",
        "Measures" : " • Check whether the medium-voltage transformer is correctly connected. • Check the temperature of the insulation oil of the medium-voltage transformer. "
        } ,
    "25" : {
        "discript" : " APU 5 / 6 cooling fluid low ",
        "cause": " The filling level of the cooling liquid is too low. ",
        "Measures" : " • Check the filling level of the cooling liquid. If the filling level is the cooling liquid is too low, replenish the cooling liquid. \n • Open the doors of cabinets +C3 and +C6.\n • Check all pipes and hoses for leaks. If leaks are found, contact the manufacturer. You will find information on this in Chapter Technical support (page 355). "
        }, 
    "26" : {
        "discript" : " Error count overrun ",
        "cause": " The number of error messages that occur within one hour has exceeded the threshold. ",
        "Measures" : " Check all faults and remedy them. "
        }, 
    "27" : {
        "discript" : " APU 1 / 2 insulation monitor failed ",
        "cause": " • The insulation monitor has an internal fault. • The software version if obsolete. ",
        "Measures" : " • Check the operating state that the insulation monitor is in. \n • Check the error messages that are output for the insulation monitor \n • Perform a software update of the APUs. "
        }, 
    "28" : {
        "discript" : " APU 3 / 4 insulation monitor failed ",
        "cause": " • The insulation monitor has an internal fault. • The software version if obsolete. ",
        "Measures" : " • Check the operating state that the insulation monitor is in.\n • Check the error messages that are output for the insulation monitor. \n • Perform a software update of the APUs. "
        }, 
    "29" : {
        "discript" : " APU 5 / 6 insulation monitor failed ",
        "cause": " • The insulation monitor has an internal fault. • The software version if obsolete. ",
        "Measures" : " • Check the operating state that the insulation monitor is in. \n• Check the error messages that are output for the insulation monitor. \n• Perform a software update of the APUs. "
        } ,
    "30" : {
        "discript" : " APU 1 Powerlink ",
        "cause": " The Powerlink interface signals more than 5 communication errors in one hour. ",
        "Measures" : " • Check the connection to the apparent power master controller. \n• Check the connection to the Ethernet switch. \n• Check the connection to the control unit. You will find information on this in Section Control unit – interior view in Chapter Design (page 32)."
        } ,
    "31" : {
        "discript" : " APU 2 Powerlink ",
        "cause": " The Powerlink interface signals more than 5 communication errors in one hour. ",
        "Measures" : " • Check the connection to the apparent power master controller. \n• Check the connection to the Ethernet switch.\n • Check the connection to the control unit. You will find information on this in Section Control unit – interior view in Chapter Design (page 32)."
        } ,
    "32" : {
        "discript" : " APU 3 Powerlink ",
        "cause": " The Powerlink interface signals more than 5 communication errors in one hour. ",
        "Measures" : " • Check the connection to the apparent power master controller. \n• Check the connection to the Ethernet switch.\n • Check the connection to the control unit. You will find information on this in Section Control unit – interior view in Chapter Design (page 32)."
        }, 
    "33" : {
        "discript" : " APU 4 Powerlink ",
        "cause": " The Powerlink interface signals more than 5 communication errors in one hour. ",
        "Measures" : " • Check the connection to the apparent power master controller. \n• Check the connection to the Ethernet switch. \n• Check the connection to the control unit. You will find information on this in Section Control unit – interior view in Chapter Design (page 32)."
        }, 
    "34" : {
        "discript" : " APU 5 Powerlink ",
        "cause": " The Powerlink interface signals more than 5 communication errors in one hour. ",
        "Measures" : " • Check the connection to the apparent power master controller. \n• Check the connection to the Ethernet switch. \n• Check the connection to the control unit. You will find information on this in Section Control unit – interior view in Chapter Design (page 32)."
        }, 
    
    "35" : {
        "discript" : " APU 6 Powerlink ",
        "cause": " The Powerlink interface signals more than 5 communication errors in one hour. ",
        "Measures" : " • Check the connection to the apparent power master controller. \n• Check the connection to the Ethernet switch. \n• Check the connection to the control unit. You will find information on this in Section Control unit – interior view in Chapter Design (page 32)."
        } ,
    "36" : {
        "discript" : " APU 1 type mismatch ",
        "cause": " An incorrect control module type has been installed. ",
        "Measures" : " • Note down the serial number of the control module. \n•   Contact the manufacturer. You will find information"
        }, 
    "37" : {
        "discript" : " APU 2 type mismatch",
        "cause": " An incorrect control module type has been installed. ",
        "Measures" : " • Note down the serial number of the control module. \n•   Contact the manufacturer. You will find information"
        }, 
    "38" : {
        "discript" : "APU 3 type mismatch ",
        "cause": " An incorrect control module type has been installed. ",
        "Measures" : " • Note down the serial number of the control module. \n•   Contact the manufacturer. You will find information"
        }, 
    "39" : {
        "discript" : " APU 4 type mismatch",
        "cause": " An incorrect control module type has been installed. ",
        "Measures" : " • Note down the serial number of the control module. \n•   Contact the manufacturer. You will find information"
        }, 
    "40" : {
        "discript" : " APU 5 type mismatch",
        "cause": " An incorrect control module type has been installed. ",
        "Measures" : " Note down the serial number of the control module. "
        }, 
    "41" : {
        "discript" : " APU 6 type mismatch",
        "cause": " An incorrect control module type has been installed. ",
        "Measures" : " Note down the serial number of the control module. "
        }, 
    "42" : {
        "discript" : " APS unlicensed ",
        "cause": " Inverter not licensed. ",
        "Measures" : " Add a licence to the software of the inverter. "
        }, 
    "43" : {
        "discript" : " Internal configuration not valid ",
        "cause": " Configuration not correct. ",
        "Measures" : " Reparameterize the inverter. "
        }, 
    "44" : {
        "discript" : " APU Update ",
        "cause": " The APU is in update mode. ",
        "Measures" : " Perform a software update of the APU. "
        }, 
    "45" : {
        "discript" : " APMC — Battery missing/empty ",
        "cause": " The battery of the apparent power master controller is missing or discharged.",
        "Measures" : " Open the miniature disconnector in the cabinet +C1. • Replace the battery. "
        }, 
    "46" : {
        "discript" : " APU1/2 Insulation Monitoring (pos. ground) ",
        "cause": " Positive ground feedback is faulty. ",
        "Measures" : " Check the position of the circuit breaker (-Q116). If the circuit breaker is in position TRIPPED, switch it to position I."
        } ,
    "47" : {
        "discript" : " APU3/4 Insulation Monitoring (pos. ground) ",
        "cause": "ositive ground feedback is faulty. ",
        "Measures" : " heck the position of the circuit breaker (-Q216). If the circuit breaker is in position TRIPPED, switch it to position I."
        } ,
    "48" : {
        "discript" : " APU1/2 Insulation Monitoring (neg. ground) ",
        "cause": " Positive ground feedback is faulty. ",
        "Measures" : " Check the position of the circuit breaker (-Q116). If the circuit breaker is in position TRIPPED, switch it to position I."
        } ,
    "49" : {
        "discript" : " APU3/4 Insulation Monitoring (neg. ground) ",
        "cause": " Positive ground feedback is faulty. ",
        "Measures" : " Check the position of the circuit breaker (-Q216). If the circuit breaker is in position TRIPPED, switch it to position I. "
        } ,
    "50" : {
        "discript" : " APU1/2 extern Insulation Monitoring",
        "cause": " Monitor feedback vom external IMD device is faulty. ",
        "Measures" : " Check if a HIGH-pulse (DC +24 V) is applied at (-KF3) port 23 (DI07) . If DC 0 V is applied, apply a HIGH-pulse (DC +24 V)."
        } ,
    "51" : {
        "discript" : " APU3/4 extern Insulation Monitoring",
        "cause": " Monitor feedback vom external IMD device is faulty. ",
        "Measures" : " Check if a HIGH-pulse (DC +24 V) is applied at (-KF3) port 24 (DI08). If DC 0 V is applied, apply a HIGH-pulse (DC 24 V). "
        } 
    
    } 
