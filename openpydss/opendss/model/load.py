from openpydss.opendss.model.dssobject import DSSObject


class Load(DSSObject):
    def __init__(
            self,
            phases="3",
            bus1="load_1",
            kV="12.47",
            kW="10",
            pf="0.88",
            model="1",
            yearly="",
            daily="",
            duty="",
            growth="",
            conn="wye",
            kvar="5.39742822138087",
            Rneut="-1",
            Xneut="0",
            status="variable",
            Class="1",
            Vminpu="0.95",
            Vmaxpu="1.05",
            Vminnorm="0.0",
            Vminemerg="0.0",
            xfkVA="0.0",
            allocationfactor="0.5",
            kVA="11.3636363636364",
            pct_mean="50",
            pct_stddev="10",
            CVRwatts="1",
            CVRvars="2",
            kwh="0",
            kwhdays="30",
            Cfactor="4",
            CVRcurve="",
            NumCust="1",
            ZIPV="",
            pct_SeriesRL="50",
            RelWeight="1",
            Vlowpu="0.5",
            puXharm="0",
            XRharm="6",
            spectrum="defaultload",
            basefreq="60",
            enabled="true",
            like="",
    ):
        super().__init__()
        self.phases = phases
        self.bus1 = bus1
        self.kV = kV
        self.kW = kW
        self.pf = pf
        self.model = model
        self.yearly = yearly
        self.daily = daily
        self.duty = duty
        self.growth = growth
        self.conn = conn
        self.kvar = kvar
        self.Rneut = Rneut
        self.Xneut = Xneut
        self.status = status
        self.Class = Class
        self.Vminpu = Vminpu
        self.Vmaxpu = Vmaxpu
        self.Vminnorm = Vminnorm
        self.Vminemerg = Vminemerg
        self.xfkVA = xfkVA
        self.allocationfactor = allocationfactor
        self.kVA = kVA
        self.pct_mean = pct_mean
        self.pct_stddev = pct_stddev
        self.CVRwatts = CVRwatts
        self.CVRvars = CVRvars
        self.kwh = kwh
        self.kwhdays = kwhdays
        self.Cfactor = Cfactor
        self.CVRcurve = CVRcurve
        self.NumCust = NumCust
        self.ZIPV = ZIPV
        self.pct_SeriesRL = pct_SeriesRL
        self.RelWeight = RelWeight
        self.Vlowpu = Vlowpu
        self.puXharm = puXharm
        self.XRharm = XRharm
        self.spectrum = spectrum
        self.basefreq = basefreq
        self.enabled = enabled
        self.like = like
