#!/usr/bin/node
/**
 * Represents a parallelogram with 4 right angles.
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

  /**
   * Prints this Rectangle with the character 'X'.
   */
  print () {
    [this.width, this.height] = [this.height, this.width];
  }
  
  /**
   * exchanges the width and height
   */
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
  
  /**
   * doubles the w and h by 2
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
