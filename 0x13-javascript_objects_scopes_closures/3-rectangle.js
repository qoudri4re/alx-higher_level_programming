
#!/usr/bin/node
/**
 * represents a rectangle
 */
class Rectangle {
  /**
   * Creates a new Rectangle with the given dimensions.
   * @param {Number} w The value of the width.
   * @param {Number} h The value of the height.
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  
    print () {
    const row = new Array(this.width).fill('X', 0, this.width);
    const rows = new Array(this.height).fill(row.join(''), 0, this.height);
    console.log(rows.join('\n'));
  }
}

module.exports = Rectangle;
