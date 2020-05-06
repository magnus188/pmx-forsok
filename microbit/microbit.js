// Variable to store magnetic force
let styrke = 0

// Create baseline by measuring background noise
let baselinhe = input.magneticForce(Dimension.X)
basic.forever(function () {
    // Measure magnetic strength and subtract background noise
    styrke = Math.abs(input.magneticForce(Dimension.Strength) - baselinhe)
    // Check if plausible value
    if (styrke > 300) {
        // PLausible value over 300
        basic.showIcon(IconNames.Giraffe)
        serial.writeString("" + styrke)
        serial.writeString(".")
    } else {
        // Not plausible value, most likely some background noise
        basic.showIcon(IconNames.StickFigure)
    }
})
