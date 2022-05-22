from openpydss.opendss.model.dssobject import DSSObject


class Generator(DSSObject):
    def __init__(
            self,
            phases="3",
            bus1="generator_1",
            kv="12.47",
            kW="1000",
            pf="0.88",
            kvar="60",
            model="1",
            Vminpu="0.90",
            Vmaxpu="1.10",
            yearly="",
            daily="",
            duty="",
            dispmode="Default",
            dispvalue="0.0",
            conn="wye",
            Rneut="0",
            Xneut="0",
            status="variable",
            Class="1",
            Vpu="1.0",
            maxkvar="120",
            minkvar="-120",
            pvfactor="0.1",
            forceon="No",
            kVA="1200",
            MVA="1.2",
            Xd="1",
            Xdp="0.28",
            Xdpp="0.2",
            H="1",
            D="0",
            UserModel="",
            UserData="()",
            ShaftModel="",
            ShaftData="()",
            DutyStart="0",
            debugtrace="no",
            Balanced="No",
            XRdp="20",
            UseFuel="No",
            FuelkWh="0",
            pct_Fuel="100",
            pct_Reserve="20",
            Refuel="No",
            spectrum="defaultgen",
            basefreq="60",
            enabled="true",
            like="",
    ):
        super().__init__()
        self.phases = phases
        self.bus1 = bus1
        self.kv = kv
        self.kW = kW
        self.pf = pf
        self.kvar = kvar
        self.model = model
        self.Vminpu = Vminpu
        self.Vmaxpu = Vmaxpu
        self.yearly = yearly
        self.daily = daily
        self.duty = duty
        self.dispmode = dispmode
        self.dispvalue = dispvalue
        self.conn = conn
        self.Rneut = Rneut
        self.Xneut = Xneut
        self.status = status
        self.Class = Class
        self.Vpu = Vpu
        self.maxkvar = maxkvar
        self.minkvar = minkvar
        self.pvfactor = pvfactor
        self.forceon = forceon
        self.kVA = kVA
        self.MVA = MVA
        self.Xd = Xd
        self.Xdp = Xdp
        self.Xdpp = Xdpp
        self.H = H
        self.D = D
        self.UserModel = UserModel
        self.UserData = UserData
        self.ShaftModel = ShaftModel
        self.ShaftData = ShaftData
        self.DutyStart = DutyStart
        self.debugtrace = debugtrace
        self.Balanced = Balanced
        self.XRdp = XRdp
        self.UseFuel = UseFuel
        self.FuelkWh = FuelkWh
        self.pct_Fuel = pct_Fuel
        self.pct_Reserve = pct_Reserve
        self.Refuel = Refuel
        self.spectrum = spectrum
        self.basefreq = basefreq
        self.enabled = enabled
        self.like = like
