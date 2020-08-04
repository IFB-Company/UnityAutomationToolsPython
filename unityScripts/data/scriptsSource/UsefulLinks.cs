using System;
using UnityEditor;
using UnityEngine;
using Object = UnityEngine.Object;

namespace GameEditorDebugHelpers
{
    public class UsefulLinks : MonoBehaviour
    {
        private static readonly string hook_name = "[HOOK_FOLDER].prefab";
        
        [MenuItem("UsefulLinks/Locations levels folder")]
        private static void OpenLocationLevelsFolder()
        {
            var path = "Assets/Prefabs/LevelSystem/Locations/" + hook_name;
            TryPingObjectbyPath(path);
        }
        
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
    } 
}

