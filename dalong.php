<?php
class DaLong {
    // 更新数组的键名
    public function replace_key($array, $oldkey, $newkey) {
        $keys = array_keys($array);
        // 考虑要替换的键名不存在的情况
        if (false === array_search($oldkey, $keys)) {
            throw new \Exception('Key ' . $oldkey . ' does not exit');
        } else {
            $keys[$oldkey] = $newkey;
            return array_combine($keys, array_values($array));
        }
    }

    // 更新二维数组键名
    public function replace_keys($array, $keyarray) {
        $keys = array_keys($keyarray);
        foreach ($keyarray as $key => $value) {
            $keys[$key] = $value;
        }
        return array_combine($keys, array_values($array));
    }
}

?>