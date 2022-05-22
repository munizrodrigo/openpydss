from openpydss.opendss.model.dssobject import DSSObject


class Line(DSSObject):
    def __init__(
            self,
            bus1="line_1",
            bus2="line_2",
            linecode="",
            length="1",
            phases="3",
            r1="0.058",
            x1="0.1206",
            r0="0.1784",
            x0="0.4047",
            C1="3.4",
            C0="1.6",
            rmatrix="[0.09813333 |0.04013333 0.09813333 |0.04013333 0.04013333 0.09813333 ]",
            xmatrix="[0.2153 |0.0947 0.2153 |0.0947 0.0947 0.2153 ]",
            cmatrix="[2.8 |-0.6 2.8 |-0.6 -0.6 2.8 ]",
            Switch="False",
            Rg="0.01805",
            Xg="0.155081",
            rho="100",
            geometry="",
            units="none",
            spacing="",
            wires="",
            EarthModel="Deri",
            cncables="",
            tscables="",
            B1="1.28177",
            B0="0.6031858",
            Seasons="1",
            Ratings="[400,]",
            LineType="oh",
            normamps="400",
            emergamps="600",
            faultrate="0.1",
            pctperm="20",
            repair="3",
            basefreq="60",
            enabled="true",
            like="",
    ):
        super().__init__()
        self.bus1 = bus1
        self.bus2 = bus2
        self.linecode = linecode
        self.length = length
        self.phases = phases
        self.r1 = r1
        self.x1 = x1
        self.r0 = r0
        self.x0 = x0
        self.C1 = C1
        self.C0 = C0
        self.rmatrix = rmatrix
        self.xmatrix = xmatrix
        self.cmatrix = cmatrix
        self.Switch = Switch
        self.Rg = Rg
        self.Xg = Xg
        self.rho = rho
        self.geometry = geometry
        self.units = units
        self.spacing = spacing
        self.wires = wires
        self.EarthModel = EarthModel
        self.cncables = cncables
        self.tscables = tscables
        self.B1 = B1
        self.B0 = B0
        self.Seasons = Seasons
        self.Ratings = Ratings
        self.LineType = LineType
        self.normamps = normamps
        self.emergamps = emergamps
        self.faultrate = faultrate
        self.pctperm = pctperm
        self.repair = repair
        self.basefreq = basefreq
        self.enabled = enabled
        self.like = like
