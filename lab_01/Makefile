all: ha dff

ha:
	ghdl -a ha.vhdl
	ghdl -a ha_tb.vhdl
	ghdl -e ha_tb
	ghdl -r ha_tb --vcd=ha.vcd

dff:
	ghdl -a dff.vhdl
	ghdl -a dff_tb.vhdl
	ghdl -e dff_tb
	ghdl -r dff_tb --vcd=dff.vcd
