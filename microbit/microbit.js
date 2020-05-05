let styrke = 0
let baselinhe = input.magneticForce(Dimension.X)
basic.forever(function () {
    styrke = Math.abs(input.magneticForce(Dimension.Strength) - baselinhe)
    if (styrke > 300) {
        basic.showIcon(IconNames.Giraffe)
        serial.writeString("" + styrke)
        serial.writeString(".")
    } else {
        basic.showIcon(IconNames.StickFigure)
    }
})
