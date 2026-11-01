
class RechargeEnergyMixin:
    def recharge_energy(self, amount: int) ->None:
        total_energy = self.energy + amount
        if total_energy > 100:
            total_energy = 100
        self.energy = total_energy
        self.save()

