# User defined variables 

class Common_var():
	w11r = True
	mobility_id = 1
	zero_it = False
	client_isolation = False
	hidden_ssid = False
	device_policy = False
	access_vlan = 1
	client_load = False
	proxy_arp = False
	max_clients = 100
	w11d = True
	w11k = True
	force_dhcp = False
	f_dhcp = True
	dhcp_option_82 = False
	client_txrx = False
	client_idle = 120
	fingerprint = True
	uncheck_fingerprint = False
	ofdm_only = False
	band_balance = False
	istrue = True
	isfalse = False
	bypassCNA = True
	
	gmtOffset = 4
	gmtOffsetMinute = 30

class Wep_var():
	key_index = 1

class Fdhcp_var():
	force_dhcp = 5

class Client_iso_var():
	client_iso = True


class Guest_multi_pass():
	pass_time = 1
	number_passes = 1

class Guest_var():
	timeout = 10
	g_timeout = 2
	grace = 5
	term_required_false = False
	term_required_true = True

class Guest_grace():
	grace = 5

class Guest_session():
	session = 2

class Guest_single_pass():
	dev_limit = 1

class Wispr_var():
	timeout =10
	grace = 1
	mac_format = 2

class Wispr_mac():
	mac_format = 0

 	
class Wispr_grace():
	grace = 3 

class Wipsr_session():
	session = 2

class Web_var():
	timeout = 10
	grace = 1

class Web_grace():
	grace = 3
class AD_var():
	globalCatalogEnabled = False
