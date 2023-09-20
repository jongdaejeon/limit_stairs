let M = ["11111", "00000", "00001", "00010", "00100", "01000", "10000", "01000", "00100", "00010", "00100", "00010", "10000", "01000", "00100", "01000", "10000"]
let height = M.length - 5
let flag_a = false
let flag_b = false
// basic.pause(100)
basic.forever(function on_forever() {
    let ib: number;
    let it: number;
    let up: boolean;
    let fail: boolean;
    
    if (height == 0) {
        return
    }
    
    let a = M.slice(height, height + 5)
    for (let y = 0; y < 5; y++) {
        for (let x = 0; x < 5; x++) {
            led.plotBrightness(x, y, parseInt(a[y][x]) * 255)
        }
        ib = a[4].indexOf("1")
        it = a[3].indexOf("1")
        up = false
        fail = false
    }
    //  check botton statue
    if (flag_a) {
        flag_a = false
        if (it < ib) {
            up = true
        } else {
            fail = true
        }
        
    }
    
    if (flag_b) {
        flag_b = false
        if (it > ib) {
            up = true
        } else {
            fail = true
        }
        
    }
    
    if (up) {
        height -= 1
    }
    
    if (fail) {
        soundExpression.sad.playUntilDone()
        height = M.length - 5
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    flag_a = true
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    flag_b = true
})
