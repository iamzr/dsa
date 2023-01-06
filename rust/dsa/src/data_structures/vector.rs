struct Vector {
    size: i32,
    capacity: i32,
    values: vec,
}

impl Default for Vector {
    fn default() -> Vector {
        Vector {
            size: 0,
            capacity: 16,
            values: [0,1]
        }
    }
}

impl Vector {
    fn size(&self) -> i32 {
        self.size
    }

    fn capacity(&self) -> i32 {
        self.capacity
    }

    fn is_empty(&self) -> i32 {
        self.size == 0
    }

    fn at(&self, index: &i32) {

    }
}

#[cfg(test)]
mod tests {
    use crate::data_structures::vector::Vector;

    #[test]
    fn test_size_given_empty_vector_returns_0() {
        let vector: Vector = Vector {};
        assert_eq!(vector.size(), 0)
    }
}