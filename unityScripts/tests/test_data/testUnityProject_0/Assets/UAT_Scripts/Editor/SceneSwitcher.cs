using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;

namespace UAT_Generated
{
	public class SceneSwitcher : MonoBehaviour
	{
		
		[MenuItem("UAT_SceneSwitcher/Main")]
		static void Load_Main()
		{
			EditorSceneManager.OpenScene("Assets/Scenes/Main.unity");
		}

		[MenuItem("UAT_SceneSwitcher/Level_1")]
		static void Load_Level_1()
		{
			EditorSceneManager.OpenScene("Assets/Scenes/Levels/Level_1.unity");
		}

		[MenuItem("UAT_SceneSwitcher/Level_0")]
		static void Load_Level_0()
		{
			EditorSceneManager.OpenScene("Assets/Scenes/Levels/Level_0.unity");
		}

	}
}