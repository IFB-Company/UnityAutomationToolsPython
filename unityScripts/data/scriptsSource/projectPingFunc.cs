        private static void TryPingObjectbyPath(string path)
        {
            Object assetInPath = GetAssetByPath(path);
            int id = -1;
            if (assetInPath != null)
            {
                id = assetInPath.GetInstanceID();
            }
            if (id <= -1)
            {
                Debug.LogError($"There is no file at path {path}!");
                return;
            }
            EditorGUIUtility.PingObject(id);
        }

        private static Object GetAssetByPath(string path)
        {
            return AssetDatabase.LoadAssetAtPath<Object>(path);
        }