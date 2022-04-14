using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace IWPandDatabase.Models
{
    public class Blocks
    {
        [Display(Name="BlockID"),Required]
        public int BlockID { get; set; }

        [Display(Name = "Nonce"), Required]
        public string Nonce { get; set; }

        [Display(Name = "Data"), Required]
        public string Data { get; set; }

        [Display(Name = "Hash"), Required]
        public string Hash { get; set; }
    }
}