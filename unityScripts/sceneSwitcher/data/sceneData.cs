using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;

namespace IFBTools.Scenes
{
    public class SceneSwitcherEditor : MonoBehaviour
    {

        [MenuItem("SceneSwitcher/Preloader")]
        static void LoadPreloader()
        {
            LoadSceneByName("Preloader");
        }


        static void LoadSceneByName(string sceneName)
        {
            EditorSceneManager.OpenScene($"Assets/Scenes/{sceneName}.unity");
        }
    }

}