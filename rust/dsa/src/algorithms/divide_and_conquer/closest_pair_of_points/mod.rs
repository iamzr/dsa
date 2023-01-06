pub struct Point {
    x: f32,
    y: f32
}

fn distance(point1: &Point, point2: &Point) -> f32 {
    ((point1.x - point2.x).powi(2) + (point1.y - point2.y).powi(2)).sqrt()
}

pub fn brute_force(points: &[Point]) -> f32 {
    let mut minimum_value: f32 = 0.0;
    let number_of_points = points.len();

    for i in 1..number_of_points {
        for j in i+1..number_of_points {
            let distance_between_i_j = distance(&points[i], &points[j]);

            if distance_between_i_j < minimum_value {
                minimum_value = distance_between_i_j  
            }
        }
    }

    minimum_value
}


#[cfg(test)]
mod tests {
    #[test]
    fn test_brute_force() {
        use super::*;

        let points: [Point; 6] = [Point { x: 2.0, y: 3.0}, Point { x: 12.0, y: 30.0},Point { x:40.0, y: 50.0},Point { x: 12.0, y: 10.0},Point { x: 3.0, y: 4.0},Point { x: 2.0, y: 3.0}];

        let result = brute_force(&points);
        assert_eq!(result, 1.414214);
    }
}